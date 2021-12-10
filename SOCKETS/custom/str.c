#include <stdlib.h>
#include <string.h>
#include <stdio.h>

const char *tmp = 'GET /get HTTP/1.1 Host: 127.0.0.1:8888  User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8  Accept-Language: en-US,en;q=0.5  Accept-Encoding: gzip, deflate  Connection: keep-alive  Upgrade-Insecure-Requests: 1  Sec-Fetch-Dest: document  Sec-Fetch-Mode: navigate  Sec-Fetch-Site: none  Sec-Fetch-User: ?1  Cache-Control: max-age=0';

int main(int argc, char *argv[]){
    char *ret;

    ret = strstr(tmp, "Host");
    if (ret)
        printf("found substring at address %p\n", ret);
    else
        printf("no substring found!\n");

    exit(EXIT_SUCCESS);
}
