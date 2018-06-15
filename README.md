# Anubis
A quantum resistant peer-to-peer instant messenger utilising cure.

**Encryption methods to maximise resistance to quantum based attacks:**

* Password encryption (Hashing and salting methods):
Hash values utilise PBKDF2 (Password-Based Key Derivation Function 2) to reduce vulnerability to brute force attacks, with a selected key to byte map of 64 and 100 encryption rounds to reduce preimage collision and vulnerability to Grover's algorithm<sup> 1</sup>. Although BCrypt is theortically not weakened by Grover's algorithm<sup> 2</sup>, this added layer of vulnerability reduction is simply a precaution. Salt values are generated randomly through BCrypt, utilising 20 rounds ensure a higher level entropy between generated salt values.

**References:**

<sup>1 </sup>https://en.wikipedia.org/wiki/Grover%27s_algorithm

<sup>2 </sup>https://cs.stackexchange.com/questions/586/could-quantum-computing-eventually-be-used-to-make-modern-day-hashing-trivial-to

<sup>2 </sup>https://stackoverflow.com/questions/2768807/quantum-computing-and-encryption-breaking
