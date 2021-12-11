#include<stdio.h>
#include<string.h>	//strlen
#include<stdlib.h>	//strlen
#include<sys/socket.h>
#include<arpa/inet.h>	//inet_addr
#include<unistd.h>	//write
#include<pthread.h> //for threading , link with lpthread
#include <netinet/in.h> /* struct sockaddr_in, struct sockaddr */
#include <netdb.h> 
//the thread function
void *connection_handler(void *);
void error(const char *msg) { perror(msg); exit(0); }

int main(int argc , char *argv[])
{
	
	// if (argc!=2){
	// 	puts("Enter port number");
	// 	exit(0);
	// }
	// int port_number = strtol(argv[0]);
	int socket_desc , client_sock , c , *new_sock;
	struct sockaddr_in server , client;
	
	//Create socket
	socket_desc = socket(AF_INET , SOCK_STREAM , 0);
	if (socket_desc == -1)
	{
		printf("Could not create socket");
	}
	puts("Socket created");
	
	//Prepare the sockaddr_in structure
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons( 8888 );
	
	//Bind
	if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
	{
		//print the error message
		perror("bind failed. Error");
		return 1;
	}
	puts("bind done");
	
	//Listen
	listen(socket_desc , 3);
	
	//Accept and incoming connection
	puts("Waiting for incoming connections...");
	c = sizeof(struct sockaddr_in);
	
	
	//Accept and incoming connection
	puts("Waiting for incoming connections...");
	c = sizeof(struct sockaddr_in);
	while( (client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c)) )
	{
		puts("Connection accepted");
		
		pthread_t sniffer_thread;
		new_sock = malloc(1);
		*new_sock = client_sock;
		
		if( pthread_create( &sniffer_thread , NULL ,  connection_handler , (void*) new_sock) < 0)
		{
			perror("could not create thread");
			return 1;
		}
		
		//Now join the thread , so that we dont terminate before the thread
		//pthread_join( sniffer_thread , NULL);
		puts("Handler assigned");
	}
	
	if (client_sock < 0)
	{
		perror("accept failed");
		return 1;
	}
	
	return 0;
}

/*
 * This will handle connection for each client
 * */
void *connection_handler(void *socket_desc)
{
	//Get the socket descriptor
	int sock = *(int*)socket_desc;
	int read_size;
	char *message , client_message[2000];
	
	
	//Receive a message from client
	while( (read_size = recv(sock , client_message , 2000 , 0)) > 0 )
	{
		//Send the message back to client

		puts(client_message); 

		// write(sock , client_message , strlen(client_message));
		//begin
		int portno =        80;
		char *host =        "192.168.0.102";
		struct hostent *server;
		struct sockaddr_in serv_addr;
		int sockfd, bytes, sent, received, total;
		char message[1024],response[4096];
		char *message_fmt = "GET /index.php/user/list?limit=20 HTTP/1.0\r\n\r\n";
		sprintf(message,client_message);
		/* create the socket */
		sockfd = socket(AF_INET, SOCK_STREAM, 0);
		if (sockfd < 0) error("ERROR opening socket");

		/* lookup the ip address */
		server = gethostbyname(host);
		if (server == NULL) error("ERROR, no such host");

		/* fill in the structure */
		memset(&serv_addr,0,sizeof(serv_addr));
		serv_addr.sin_family = AF_INET;
		serv_addr.sin_port = htons(portno);
		memcpy(&serv_addr.sin_addr.s_addr,server->h_addr,server->h_length);

		/* connect the socket */
		if (connect(sockfd,(struct sockaddr *)&serv_addr,sizeof(serv_addr)) < 0)
			error("ERROR connecting");

		/* send the request */
		total = strlen(message);
		sent = 0;
		do {
			bytes = write(sockfd,message+sent,total-sent);
			if (bytes < 0)
				error("ERROR writing message to socket");
			if (bytes == 0)
				break;
			sent+=bytes;
		} while (sent < total);

		/* receive the response */
		memset(response,0,sizeof(response));
		total = sizeof(response)-1;
		received = 0;
		do {
			bytes = read(sockfd,response+received,total-received);
			if (bytes < 0)
				error("ERROR reading response from socket");
			if (bytes == 0)
				break;
			received+=bytes;
		} while (received < total);

		/*
		* if the number of received bytes is the total size of the
		* array then we have run out of space to store the response
		* and it hasn't all arrived yet - so that's a bad thing
		*/
		if (received == total)
			error("ERROR storing complete response from socket");

		/* close the socket */
		close(sockfd);

		/* process response */
		//end
		write(sock , response , strlen(response));
		
		memset(client_message, 0, strlen(client_message));
		
		
	}
	
	if(read_size == 0)
	{
		puts("Client disconnected");
		fflush(stdout);
	}
	else if(read_size == -1)
	{
		perror("recv failed");
	}
		
	//Free the socket pointer
	free(socket_desc);
	
	return 0;
}
