// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "../src/Contract.sol";
import "forge-std/Test.sol";

contract ContractTest is Test {
    Contract public myContract;
    function setUp() public {
        myContract = new Contract();
    }

    function testInitializedCorrectly() public {
        assertTrue(myContract.number() == 0);

        myContract.setNumber(777);

        assertTrue(myContract.number() == 777);
    }
}
