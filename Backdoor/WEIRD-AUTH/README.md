Backdoor: WEIRD-AUTH
--------------------------------

https://backdoor.sdslabs.co/challenges/WEIRD-AUTH

The challenge asks us to try to gain access to the admin account. The obvious
first thing to do is to inspect the source of the webpage. Besides the login 
inputs, there doesn't seem to be much to play around with except for a 
suspicious icon in the HTML head. However, upon downloading the icon and running 
it briefly through some online gif forensics tools, there doesn't seem to be
anything special with the gif. Considering the fact that the problem is 150
points, it's also unlikely the challenge will be that easy.

The next logical step seemed to be exploiting some sort of vulnerability in the
input validation, e.g with SQL injection or by submitting PHP code to see if the 
input values are ever evaluated. However, after a few rounds of trial and error
it appeared that this would not work as well. As long as the username isn't
`admin` (which, presumably, we are trying to get access to) nor `vampire`, the
username is essentially echoed back to us in the logged in page. Likewise, the
password didn't seem to produce any obvious side effects.

In the process of logging in with various dummy usernames, however, one notable 
thing was that the cookie was being set to a common string postfixed with a 
unique sequence of characters (one could obtain the cookie by inspecting the
HTTP headers, or, alternatively, printing the value of `document.cookie` in the
web console). For instance, when logging in with username "asdf", the cookie 
would be set to "session=6f61736469303833686a64616e6d6164666f77753061736466",
whereas when logging in with username "hello", the cookie would be set to 
"session=6f61736469303833686a64616e6d6164666f77753068656c6c6f". As it turns out, 
both cookies share the prefix "6f61736469303833686a64616e6d6164666f777530", 
with the unique postfixed sequence being the hex encoding of the username (more  
concretely, the "61736466" of the first cookie is the hex equivalent of "asdf").
With this, we can easily gain access to the admin account, by simply setting the
cookie to be "6f61736469303833686a64616e6d6164666f77753061646d696e".

Once in the admin account, everything is ostensibly the same. However, after 
poking around in the HTML a bit logner, the suspicious icon tag in the head 
noticeably refers to a different image, "icon256.gif", as opposed to "icon.gif" 
from before. A common technique with concealing data within images is appending 
the bytes of a different file to the end of the image. An image with extra bytes 
appended will behave largely the same as the original as long as the image 
header and footer are left intact. Indeed, a quick inspection of the sizes of 
"icon256.gif" and "icon.gif" reveals that "icon256.gif" is indeed larger.
Further, if we diff the hex dumps of the two images, we see that "icon256.gif" 
is actually the exact same as "icon.gif" with extra bytes appended to it. If we 
extract those extra bytes into its own file, and run the `file` command on it, 
we see that the bytes actually constitute a `zip` archive. 

Running the file through an unarchiver, we are left with a folder containing a 
`class` file. The `class` file itself isn't too helpful, although it's easily to
decompile (there are online tools to do this). The decompilation results in the
following code:

```
import java.io.PrintStream;
import java.security.MessageDigest;

public static void main(String[] arrstring) throws Exception {
    String string = "U0hBMjU2ezYxZl8xNV9uMWMzXzcwX2gxZDNfbXlfajR2NF9wcjA2cjRtfQ==";
    byte[] arrby = string.getBytes("UTF-8");
    MessageDigest messageDigest = MessageDigest.getInstance("MD5");
    byte[] arrby2 = messageDigest.digest(arrby);
    String string2 = new String(arrby2);
    System.out.println("Flag is " + string2);
}
```

Running the program as is, however, we find that the value of `string2` as well 
as the `sha256` of `string2` don't yield the correct flag. The last piece of the 
puzzle is realizing that the `md5` computation is misdirection -- the variable 
`string` is actually just the `base64` encoding of the flag (as hinted by the
trademark `==` of `base64` strings). Indeed, if we `base64` decode the string, 
we are left with the flag.
