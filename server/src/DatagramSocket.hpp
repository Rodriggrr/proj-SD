#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string>
#include <thread>

using sock_t = int;

class RequestTimedOut : public std::exception {
public:
    const char* what() const noexcept override {
        return "Request timed out";
    }
};

/**
 * @brief DatagramSocket class
 * @param port needed
 * @param address optional
 * @param timeout optional
 * @param maxConnectionsQueue optional
*/
class DatagramSocket {
    sock_t sock;
    sockaddr_in address;
    std::string ip;
    char buffer[1024];
    int port;
    int timeout;
    int maxConnectionsQueue;

    void bind() {
        sock = socket(AF_INET, SOCK_DGRAM, 0);
        if (sock < 0) {
            throw std::runtime_error("Failed to create socket");
        }

        int opt = 1;
        if (setsockopt(sock, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
            throw std::runtime_error("Failed to set socket options");
        }

        address.sin_family = AF_INET;
        address.sin_addr.s_addr = inet_addr(this->ip.c_str());
        address.sin_port = htons(this->port);

        if (::bind(sock, (sockaddr*)&address, sizeof(address)) < 0) {
            throw std::runtime_error("Failed to bind socket");
        }

    }

public:
    DatagramSocket(int port, std::string ip = "0.0.0.0", int timeout = 0, int maxConnectionsQueue = 10){
        this->port = port;
        this->ip = ip;
        this->timeout = timeout;
        this->maxConnectionsQueue = maxConnectionsQueue;
        bind();
    }

    /**
     * @brief set timeout for socket
     * @param timeout in milliseconds
    */
    void setSoTimeout(int timeout){
        this->timeout = timeout;

        int opt = timeout;
        if (setsockopt(sock, SOL_SOCKET, SO_RCVTIMEO, &opt, sizeof(opt))) {
            throw std::runtime_error("Failed to set socket options");
        }
    }

    /**
     * @brief send message to address
     * @param address
     * @param message
    */
    void sendTo(sockaddr_in& address, std::string message) {
        if (sendto(sock, message.c_str(), message.size(), 0, (sockaddr*)&address, sizeof(address)) < 0) {
            throw std::runtime_error("Failed to send message");
        }
    }

    std::pair<int, char*> recv() {
        socklen_t len = sizeof(address);
        int valread = recvfrom(sock, buffer, 1024, 0, (sockaddr*)&address, &len);
        if (valread < 0) {
            throw std::runtime_error("Failed to receive message");
        }
        return std::make_pair(valread, buffer);
    }

    sockaddr_in* getAddress(){
        return &address;
    }
};