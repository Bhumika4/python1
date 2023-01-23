{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c566ebe8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram's account balance 20000\n",
      "depsitted amount 10000 \n",
      "ram's account balance 30000\n",
      "transaction completed\n",
      "ram's account balance 25000\n",
      "insufficient balance\n"
     ]
    }
   ],
   "source": [
    "class bank:\n",
    "    bname=\"sbi\"\n",
    "    nob=123\n",
    "    roi=0.09\n",
    "    def __init__(self,name,accno,bal):\n",
    "        self.name=name\n",
    "        self.accno=accno\n",
    "        self.bal=bal\n",
    "    def checkbal(self):\n",
    "        print(f\"{self.name}'s account balance {self.bal}\")\n",
    "    def deposit(self,amt):\n",
    "        self.bal+=amt\n",
    "        print(f\"depsitted amount {amt} \")\n",
    "        print(f\"{self.name}'s available balance {self.bal}\")\n",
    "    def withdraw(self,amt):\n",
    "        if self.bal>=amt:\n",
    "            self.bal-=amt\n",
    "            print(f\"transaction completed\")\n",
    "            print(f\"{self.name}'s available balance {self.bal}\")\n",
    "        else:\n",
    "            print(f\"insufficient balance\")\n",
    "        \n",
    "    \n",
    "c1=bank(\"ram\",12345678,20000)\n",
    "c2=bank(\"sam\",12347658,30000)\n",
    "c1.checkbal()\n",
    "c1.deposit(10000)\n",
    "c1.withdraw(5000)\n",
    "c1.withdraw(40000)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "39658674",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f180b33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ram's account balance 20000\n",
      "depsitted amount 10000 \n",
      "ram's account balance 30000\n",
      "transaction completed\n",
      "ram's account balance 25000\n",
      "insufficient balance\n",
      "0.09-0.09\n",
      "change of roi\n",
      "0.06-0.06\n"
     ]
    }
   ],
   "source": [
    "class bank:\n",
    "    bname=\"sbi\"\n",
    "    nob=123\n",
    "    roi=0.09\n",
    "    def __init__(self,name,accno,bal):\n",
    "        self.name=name\n",
    "        self.accno=accno\n",
    "        self.bal=bal\n",
    "    def checkbal(self):\n",
    "        print(f\"{self.name}'s account balance {self.bal}\")\n",
    "    def deposit(self,amt):\n",
    "        self.bal+=amt\n",
    "        print(f\"depsitted amount {amt} \")\n",
    "    def withdraw(self,amt):\n",
    "        if self.bal>=amt:\n",
    "            self.bal-=amt\n",
    "            print(f\"transaction completed\")\n",
    "        else:\n",
    "            print(f\"insufficient balance\")\n",
    "    @classmethod\n",
    "    def checkroi(cls,roi):\n",
    "        cls.roi=roi\n",
    "        print('change of roi')\n",
    "    \n",
    "c1=bank(\"ram\",12345678,20000)\n",
    "c2=bank(\"sam\",12347658,30000)\n",
    "c1.checkbal()\n",
    "c1.deposit(10000)\n",
    "c1.checkbal()\n",
    "c1.withdraw(5000)\n",
    "c1.checkbal()\n",
    "c1.withdraw(40000)\n",
    "print(c1.roi,c2.roi,sep='-')\n",
    "c1.checkroi(0.06)\n",
    "print(c1.roi,c2.roi,sep='-')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e93d1e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter 4 digits pin:1234\n",
      "ram's account balance 20000\n",
      "enter 4 digits pin:1256\n",
      "depsitted amount 10000 \n",
      "sam's available balance 40000\n",
      "enter 4 digits pin:1256\n",
      "transaction completed\n",
      "sam's available balance 35000\n"
     ]
    }
   ],
   "source": [
    "class bank:\n",
    "    bname=\"sbi\"\n",
    "    nob=123\n",
    "    roi=0.09\n",
    "    def __init__(self,name,accno,bal,pin):\n",
    "        self.name=name\n",
    "        self.accno=accno\n",
    "        self.bal=bal\n",
    "        self.pin=pin\n",
    "    def checkbal(self):\n",
    "        if self.pin==self.checkpin():\n",
    "            print(f\"{self.name}'s account balance {self.bal}\")\n",
    "        else:\n",
    "            print('incorrect pin')\n",
    "    def deposit(self,amt):\n",
    "        if self.pin==self.checkpin():\n",
    "            self.bal+=amt\n",
    "            print(f\"depsitted amount {amt} \")\n",
    "            print(f\"{self.name}'s available balance {self.bal}\")\n",
    "        else:\n",
    "            print('incorrect pin')\n",
    "    def withdraw(self,amt):\n",
    "        if self.pin==self.checkpin():\n",
    "            if self.bal>=amt:\n",
    "                self.bal-=amt\n",
    "                print(f\"transaction completed\")\n",
    "                print(f\"{self.name}'s available balance {self.bal}\")\n",
    "            else:\n",
    "                print(f\"insufficient balance\")\n",
    "        else:\n",
    "            print('incorrect pin')\n",
    "    @staticmethod\n",
    "    def checkpin():\n",
    "        return int(input('enter 4 digits pin:'))\n",
    "    \n",
    "c1=bank(\"ram\",12345678,20000,1234)\n",
    "c2=bank(\"sam\",12347658,30000,1256)\n",
    "c1.checkbal()\n",
    "c2.deposit(10000)\n",
    "c2.withdraw(5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d0b2a089",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter 4 digits pin:1234\n",
      "count=0\n",
      "ram's account balance 20000\n",
      "enter 4 digits pin:1256\n",
      "depsitted amount 10000 \n",
      "sam's available balance 40000\n",
      "enter 4 digits pin:1256\n",
      "transaction completed\n",
      "sam's available balance 35000\n"
     ]
    }
   ],
   "source": [
    "class bank:\n",
    "    bname=\"sbi\"\n",
    "    nob=123\n",
    "    roi=0.09\n",
    "    count=0\n",
    "    def __init__(self,name,accno,bal,pin):\n",
    "        self.name=name\n",
    "        self.accno=accno\n",
    "        self.bal=bal\n",
    "        self.pin=pin\n",
    "    def checkbal(self):\n",
    "        if self.pin==self.checkpin():\n",
    "            print(f\"count={self.count}\")\n",
    "            print(f\"{self.name}'s account balance {self.bal}\")\n",
    "        else:\n",
    "            print('incorrect pin')\n",
    "            if self.count<=2:\n",
    "                self.count+=1\n",
    "                self.checkbal()\n",
    "            else:\n",
    "                print('pin entered incorrect for more than 3 times')\n",
    "                print('your account is blocked')\n",
    "    def deposit(self,amt):\n",
    "        if self.pin==self.checkpin():\n",
    "            self.bal+=amt\n",
    "            print(f\"depsitted amount {amt} \")\n",
    "            print(f\"{self.name}'s available balance {self.bal}\")\n",
    "        else:\n",
    "            print('incorrect pin')\n",
    "            print('incorrect pin')\n",
    "            if self.count<=2:\n",
    "                self.count+=1\n",
    "                self.checkbal()\n",
    "            else:\n",
    "                print('pin entered incorrect for more than 3 times')\n",
    "                print('your account is blocked')\n",
    "    def withdraw(self,amt):\n",
    "        if self.pin==self.checkpin():\n",
    "            if self.bal>=amt:\n",
    "                self.bal-=amt\n",
    "                print(f\"transaction completed\")\n",
    "                print(f\"{self.name}'s available balance {self.bal}\")\n",
    "            else:\n",
    "                print(f\"insufficient balance\")\n",
    "        else:\n",
    "            print('incorrect pin')\n",
    "            print('incorrect pin')\n",
    "            if self.count<=2:\n",
    "                self.count+=1\n",
    "                self.checkbal()\n",
    "            else:\n",
    "                print('pin entered incorrect for more than 3 times')\n",
    "                print('your account is blocked')\n",
    "    @staticmethod\n",
    "    def checkpin():\n",
    "        return int(input('enter 4 digits pin:'))\n",
    "    \n",
    "c1=bank(\"ram\",12345678,20000,1234)\n",
    "c2=bank(\"sam\",12347658,30000,1256)\n",
    "c1.checkbal()\n",
    "c2.deposit(10000)\n",
    "c2.withdraw(5000)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e94f8c07",
   "metadata": {},
   "source": [
    "###### "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "vscode": {
   "interpreter": {
    "hash": "ad2bdc8ecc057115af97d19610ffacc2b4e99fae6737bb82f5d7fb13d2f2c186"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
