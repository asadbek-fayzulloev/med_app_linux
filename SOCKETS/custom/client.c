/*
	C ECHO client example using sockets
*/
#include <stdio.h>	//printf
#include <string.h>	//strlen
#include <sys/socket.h>	//socket
#include <arpa/inet.h>	//inet_addr
#include <unistd.h>

int main(int argc , char *argv[])
{
	int sock;
	struct sockaddr_in server;
	char message[1000] , server_reply[2000];
    char ipaddr[15];

    
	
	//Create socket
	sock = socket(AF_INET , SOCK_STREAM , 0);
	if (sock == -1)
	{
		printf("Could not create socket");
	}
	puts("Socket created");

    printf("Enter ip address with dots:");
    scanf("%s", ipaddr);
	
	server.sin_addr.s_addr = inet_addr(ipaddr);
	server.sin_family = AF_INET;
	server.sin_port = htons( 8888 );
    memset(&(server.sin_zero), '\0', 8);


	//Connect to remote server
	if (connect(sock , (struct sockaddr *)&server , sizeof(server)) < 0)
	{
		perror("connect failed. Error");
		return 1;
	}
	
	puts("Connected\n");
	
	//keep communicating with server
	while(1)
	{
		printf("Enter message : ");
		scanf("%s" , message);
		
		//Send some data
		if( send(sock , message , strlen(message) , 0) < 0)
		{
			puts("Send failed");
			return 1;
		}
		else
		{
			memset(message, 0, strlen(message));
		}

		
		
		//Receive a reply from the server
		if( recv(sock , server_reply , 2000 , 0) < 0)
		{
			puts("recv failed");
			break;
		}
		else
		{
			puts("Server reply :");
			puts(server_reply);
			memset(server_reply,0,strlen(server_reply));
		}
		
		

	}
	
	close(sock);
	return 0;
}