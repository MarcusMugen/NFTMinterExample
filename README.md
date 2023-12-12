<div align="center">
    <h1>Cartesi NFT-Minter Example</h1>
    <i>An NFT-Minter using Sunodo and Cartesi Rollups</i>
</div>
<div align="center">
  This repository contains an example of an NFT-Minter writen in Python for Cartesi Rollups, with Sunodo.
</div>

<div align="center">
  
  <a href="">[![Static Badge](https://img.shields.io/badge/cartesi--rollups-1.0.0-5bd1d7)](https://docs.cartesi.io/cartesi-rollups/)</a>
  <a href="">[![Static Badge](https://img.shields.io/badge/sunodo-0.9.5-blue)](https://docs.sunodo.io/guide/introduction/what-is-sunodo)</a>
  <a href="">[![Static Badge](https://img.shields.io/badge/python-3.11-yellow)](https://www.python.org/)</a>
  <a href="">[![Static Badge](https://img.shields.io/badge/react-18.1.0-red)](https://react.dev/)</a>
</div>

## Overview

This sample dApp is a full-stack development solution that facilitates the creation (minting) of NFTs (Non-Fungible Tokens) on the blockchain through Cartesi Rollups, using Sunodo. As a standard full stack web application, it has two main block: frontend and backend. The frontend gives a integrated interface for the user to interact with the backend. Follow the steps below to build this solution end-to-end.

### Key Features

1. **Minting NFTs**: Automatically mints NFTs when a "create" command is received.
2. **Hexadecimal Encoding and Decoding**: Efficiently handles hexadecimal data conversion, crucial for blockchain interactions.
3. **Sending Notices and Vouchers**: Implements functionality to send various types of data back to the Cartesi Rollups layer.
4. **User UI**: Implements a interface to facilitate the interactions of the user with the dapp backend.


## Environment Setup - Requirements

To use this dApp, you need to set up your environment for Cartesi Rollups development with Sunodo. Below are the links to guide you through the environment setup:

1. **DevGuide**: [The Developers' Full Guide](https://github.com/cartesi/DevGuide)
2. **Sunodo**: [Installing Sunodo](https://docs.sunodo.io/guide/introduction/installing)


## Running

With a straightfoward approach, to run this solution you have to mount the [frontend](./frontend/README.md) and the [backend](./backend/README.md).

### Create the NFT - Sending inputs and executing vouchers

With the to parts running you can send the 'create' payload in the inputbox at the send option:

This will process the function that is responsible to create a voucher for the NFT. After that, you can check the voucher options and execute it.

### Notices

You can also see the list of the past queries to the backend loading the notice list in the option button at the Notice field:

