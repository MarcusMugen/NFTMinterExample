<div align="center">
    <h1>Cartesi NFT-Minter Example</h1>
    <i>An NFT-Minter using Sunodo and Cartesi Rollups</i>
</div>
<div align="center">
  This repository contains an example of an NFT-Minter writen in Python for Cartesi Rollups, with Sunodo.
</div>

<div align="center">
  
  <a href="">[![Static Badge](https://img.shields.io/badge/cartesi--rollups-1.0.0-5bd1d7)](https://docs.cartesi.io/cartesi-rollups/)</a>
  <a href="">[![Static Badge](https://img.shields.io/badge/sunodo-0.9.5-blue
)</a>
  <a href="">[![Static Badge](https://img.shields.io/badge/python-3.11-yellow)](https://www.python.org/)</a>
</div>

## Overview

This Python dApp is designed to work with Cartesi Rollups, a layer-2 solution for scalable and low-cost blockchain applications. The script facilitates the creation (minting) of NFTs (Non-Fungible Tokens) on the blockchain through Cartesi Rollups.

### Key Features

1. **Minting NFTs**: Automatically mints NFTs when a "create" command is received.
2. **Hexadecimal Encoding and Decoding**: Efficiently handles hexadecimal data conversion, crucial for blockchain interactions.
3. **Sending Notices and Vouchers**: Implements functionality to send various types of data back to the Cartesi Rollups layer.


## Environment Setup

To use this dApp, you need to set up your environment for Cartesi Rollups development with Sunodo. Below are the links to guide you through the environment setup:

1. **DevGuide**: [The Developers' Full Guide](https://github.com/cartesi/DevGuide)
2. **Sunodo**: [Installing Sunodo](https://docs.sunodo.io/guide/introduction/installing)
3. **Docs Cartesi**: [Cartesi Rollups Docs](https://docs.cartesi.io/cartesi-rollups/overview/)

## Building the dApp

Considering you followed the steps for installing Sunodo, it is straightfoward to build all the necessary to run this backend. Just run the command bellow:

```
sunodo build
```

## Running the dApp

You can use the command below to run the dApp with different behaviors:

```
sunodo run
```

will run it with the standard configurations. But you also can run it with verbose mode below.

```
sunodo run --verbose
```

You also can run it with the --epoch-duration with a low epoch duration. This is needed to execute the vouchers. Let's say we want our epoch duration to be 30 seconds:


```
sunodo run --epoch-duration 30
```

## Additional Notes

For detailed instructions and troubleshooting, refer to the Sunodo user guide and FAQs.