# (De-Authentication Attack) Management Frame Packet Attack 
## Introduction
In this lab, we will be creating a management frame attack of deauthentication a client from the AP. Then, taking advantage of the client trying to reassociate with the AP and capturing the EAPOL packets that contain the password. This will bring us to the second part of the lab, where we will use the captured packets and bruteforce it using Aircrack-ng with a customized wordlist.
_For Educational Purposes Only_
## Task 1
### What is the BSSID of the access point?
**BSSID:** C8:3A:35:02:76:30

### What is the channel of the access point?
**Channel:** 6

**AUTh:** PSK

### What is the MAC address of the device that is already connected to the access point? 
**MAC Address:** 0A:7C:AF:CA:B8:E6

![lab1](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/e824e846-eac4-43f7-a278-a40892637a8f)

**Deauthentication command**

![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/38fd50ab-b34f-4b84-a968-e4b7d90a7c2f)
**Deauthentication Packets**

![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/18113a31-4f2b-4ef3-8bfe-05c0b6b45a2b)

## Task 2 – Cracking Password
### Handshake
#### What does the first packet in the 4-way handshake authentication of WPA-PSK contain? Is it sent by the access point or the client device? What will the receiving device do with this information?  
The first packet is sent by the AP “TendaTec”. It contains the ANounce of the AP. The client receiving this will use it to construct a PTK.
![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/42515775-c67c-4866-a661-acfe07d8599a)
#### What does the second packet in the 4-way handshake authentication of WPA-PSK contain? What will the receiving device do with this information? Is it sent by the access point or the client device?
The second packet is sent from the client to the AP, it contains the SNounce and the MIC. The receiving AP will use it to construct the PTK.
![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/c19952a0-d3fe-488b-91c4-74d747d114a5)
#### What does the third packet in the 4-way handshake authentication of WPA-PSK contain? Is it sent by the access point or the client device? 
The third packet is sent by the AP to the client. It contains the GTK and MIC. “RSC” is the starting number of GTK.
![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/d965e32e-564e-417f-9526-468ef8b03a4f)
#### What does the fourth packet in the 4-way handshake authentication of WPA-PSK contain? Is it sent by the access point or the client device?
The fourth packet is sent by the client to the AP. It is an ACK packet.
![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/ece3b948-d0e2-4f36-965f-c28509dcb8ff)

### Password Cracking
#### What is the password?
**Password:** CY20sec23GMU

![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/6124db7b-f0c5-442a-a186-69aa8aea202a)

## Wordlist Generation
In summary, generating all the possible combinations is the major idea. Since we were given all the parameters, we just had to follow them to construct the wordlist. I first wrote all the possible combinations of words. Sequentially, I used a Python code to generate all the possible combinations of upper and lower case for each letter - for each string. Further, I used a Python code that will incorporate the numbers through a double loop. Finally, I tried brute-forcing the pcap password with each wordlist I generated.

### Base Dictionary:
The password can be two of the three words; hence, it must be one of the following bases:
- MASONCYSE
- MASONGMU
- CYSEMASON
- CYSEGMU
- GMUCYSE
- GMUMASON

### The math:
Since each letter can be either upper or lower case, then:
- MASONCYSE = 9 letters
- MASONGMU = 8 letters 
- CYSEMASON = 9 letters
- CYSEGMU = 7 letters
- GMUCYSE = 7 letters
- GMUMASON = 8 letters

The total possibilities for upper and lower case for each base are the following:
- 2^9 = 512
- 2^8 = 256
- 2^7 = 128

2(512) + 2(256) + 2(128) = 1792 total possibilities for upper and lower cases for the base words.

I used ChatGPT to write me the following code that will print me all the combinations for upper and lower cases. I ran the code for each base string.

### Python file: 
cases.py

### Output files:
- masoncyse.txt
- masongmu.txt
- cysemason.txt
- cysegmu.txt

After checking the outputs of each string, I checked that the total output matches the predicted combinations calculations made earlier.

### The words will always have these numbers:
1. 20 
2. 21 
3. 22 
4. 23 
5. 24

Now, since we have 512 variations for MASONCYSE upper and lower cases, we also must calculate the possibility of variation of each line with these numbers. Using the permutation formula (order-sensitive; meaning that (20,21) is a different variation from (21,20)), I found that there are 20 variations:

- (20, 21)
- (20, 22)
- (20, 23)
- (20, 24)
- (21, 20)
- (21, 22)
- (21, 23)
- (21, 24)
- (22, 20)
- (22, 21)
- (22, 23)
- (22, 24)
- (23, 20)
- (23, 21)
- (23, 22)
- (23, 24)
- (24, 20)
- (24, 21)
- (24, 22)
- (24, 23)

Now we consider the different index positions in the base word index.

`[1]M[2]A[3]S[4]O[5]N[6]C[7]Y[8]S[9]E[10]`

For each number, there are 10 different index values, but we have two numbers. So, the variations are much greater than that. 

If we calculate the total number of these numbers with one variation of ‘MASONCYSE’ then the total possibilities will be 10,626,577,920.

We need to do the same for each of the 512 variations.
10,626,577,920 * 512 = 5.4408079e+12 

So, using ChatGPT, I used a Python code that double loops around the string with the number’s permutations. I ran the strings lists for each base dictionary through this code to get the final list file for each string. The output from here will be the final wordlist used in Aircrack-ng.

### Python file: 
numbers.py

### Output files:
- Cysegmu_output.lst
- Cysemason_output.lst
- Masoncyse_output.lst
- Masongmu_output.lst

### Cracking Attempts

#### String 1: Mason Cyse

#### String 2: Mason Gmu

#### String 3: CYSEMASON

![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/4160fd72-cf97-4cfe-a834-ba7e19dd595a)

#### String 4: CYSEGMU

**Password:** CY20sec23GMU

![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/28cc99ab-772e-4b79-a35e-7c0dc52dfbd4)

## Bonus – Decrypting the Captured Packets Using the Password Gained
If the client had any communication, we would have been able to view them, decrypt them, and read them in plaintext. However, we did not continue to capture any data after getting the EAPOL. The device also didn’t have internet access, so we wouldn’t have captured any important data in this case. This might have been more beneficial in other scenarios.

![image](https://github.com/alduralmknoon/WiFi-Deauthentication-Lab/assets/27437815/d9fe2736-1f37-4c59-bf24-da05dc1faf43)
