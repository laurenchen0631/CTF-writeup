> There is a locked door in front of us that can only be opened with the secret passphrase. There are no keys anywhere in the room, only this .txt. There is also a writing on the wall.. "State 0: 69420, State N: 999, flag ends at state N, key length: one".. Can you figure it out and open the door?

1. After observing `deterministic.txt`, the format seems like a linked list. According to the description, its head id is `69420` and the last id is `999`. Also, the value of the nodes is encrypted using `xor` with a key character.

2. We created a python script to read the file and save the linked list.

3. We brute force all possible one-sized key and we got the answer.