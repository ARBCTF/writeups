https://backdoor.sdslabs.co/challenges/FAULT

Lets just include the code here:

```
#include <stdio.h>
#include <fcntl.h>

void secure_function(char* secret,char* input, char* key){
	int i;
	int secret_key=100;
	for (i = 0; i < 10; i++) {
		input[i]^=(key[i]^secret_key);
	}
	if ( !strncmp(input,secret,10) ){
		system("/bin/cat flag");
	}
	else{
		printf("Told you it's secure as :P\n");
	}
}

int main(int argc, char* argv[]){
	int fd,len;
	if (fd=open("password",O_RDONLY,0400) < 0) {
		printf("can't open password\n");
		return 0;
	}
	printf("Complex encryptions always take time...\n");
	sleep(time(0)%15);

	char secret[11];
	if(!(len=read(fd,secret,10) > 0)){
		printf("read error\n");
		close(fd);
		return 0;
	}

	char password[11];
	printf("Password : ");
	scanf("%10s", password);

	char key[11];
	printf("Key : ");
	scanf("%10s", key);

	//secure hash function
	secure_function(secret,password,key);

	close(fd);
	return 0;
}
```

We considered many possibilities here before arriving at the answer.

There's the obvious quick glance for buffer overflows or format string
vulnerabilities, but there doesn't appear to be any.

Next we considered some kind of timing attack, or other side-channels, but the
`sleep` call prevents that (and that seems overkill for this problem).

Then we put on our math hats and dug into the XOR operations for a bit. This
seems obviously wrong since the `secret` will still remain secret despite any
bit fiddling.

Hmm, so what could it be... We sat around scratching our heads for a few
minutes. Finally we noticed that for some reason the connection would hang
waiting on input before asking for the password. We'd have to hit enter to
get prompted for the password. Then we took a closer look at the following code:

```
if (fd=open("password",O_RDONLY,0400) < 0) {
    printf("can't open password\n");
    return 0;
}
```

Aha! The `<` operator takes greater precedence than the `=` operator!

The `open` call will never return a file descriptor less than `0`, so `fd`
will always end up being `0`. Remember that the `0` file descriptor corresponds
to `stdin`, so now we control `secret` in the following code:

```
if(!(len=read(fd,secret,10) > 0)){
	printf("read error\n");
	close(fd);
	return 0;
}
```

Since `fd` is `stdin` and we control `stdin` then we can put whatever we want
in `secret`!

But we're not quite done yet...

We still have to deal with this mess:

```
int secret_key=100;
for (i = 0; i < 10; i++) {
	input[i]^=(key[i]^secret_key);
}
```

First, `100` -> `0x64` -> `'d'`.

So setting `key` to `'dddddddddd'` and making `secret` and `input` the same
thing should get it done.

Lets try it out:

```
$ nc hack.bckdr.in 8012
Complex encryptions always take time...
abcdefghij
Password : abcdefghij
Key : dddddddddd
Flag is SHA256{Pwn1N9_15_MY_N1Nj4_w4y}
```

Voila!
