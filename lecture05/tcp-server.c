/**
 * TCP Server
 */

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h> 

int main(int argc, char *argv[]) {
    int listenfd = 0, connfd = 0;
    struct sockaddr_in serv_addr; 

    char sendBuff[1025];
    time_t ticks; 

    // The call to the function ‘socket()’ creates an
    // UN-named socket inside the kernel and returns an 
    // integer known as socket descriptor.
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serv_addr, '0', sizeof(serv_addr));
    memset(sendBuff, '0', sizeof(sendBuff)); 

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(5000); 

    // The call to the function ‘bind()’ assigns the details 
    // specified in the structure ‘serv_addr’ to the socket created 
    // in the step above. The details include, the family/domain, 
    // the interface to listen on(in case the system has multiple 
    // interfaces to network) and the port on which the server will 
    // wait for the client requests to come.
    bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)); 

    // The call to the function ‘listen()’ with second argument 
    // as ’10’ specifies maximum number of client connections that 
    // server will queue for this listening socket.
    listen(listenfd, 10); 
    // After the call to listen(), this socket becomes a fully 
    // functional listening socket.

    // the server is always running and the delay or sleep of 1 sec 
    // ensures that this server does not eat up all of your CPU 
    // processing.
    while(1) {
        // In the call to accept(), the server is put to sleep and 
        // when for an incoming client request, the three way TCP 
        // handshake* is complete, the function accept () wakes up 
        // and returns the socket descriptor representing the client 
        // socket.
        connfd = accept(listenfd, (struct sockaddr*)NULL, NULL);

        // As soon as server gets a request from client, it prepares 
        // the date and time and writes on the client socket through 
        // the descriptor returned by accept().

        ticks = time(NULL);
        snprintf(sendBuff, sizeof(sendBuff), "%.24s\r\n", ctime(&ticks));
        write(connfd, sendBuff, strlen(sendBuff)); 

        close(connfd);
        sleep(1);
     }
}