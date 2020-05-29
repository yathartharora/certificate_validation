# certificate_validation

Often organisations issue certificates for events they organize. However,the cetificates can easily be forged as there is no authentication criteria. This application is a prototype for certificate generator and validator.

# How the system works?

The core technology for the validation is Blockchain. Each certificate is uploaded on a decentralized system IPFS and can easily be seen and accessed by anyone across the world by using a unique hash. Each certificate contains the participant's name and a unique hash. This hash and other metadata (name, IPFS unique hash) is stored onto the blockchain network. If a person wants to verify that the certificate is valid or an official certificate, the person can simply contact the organization and give them the unique hash i.e. is printed onto the certificate. The organisation hence matches the person's name and the hash onto their blockchain network and can easily verify if the certificate is official or forged.

# Accessing the certificate

The certificate can be accessed using the link https://gateway.ipfs.io/ipfs/(your ipfs hash)
