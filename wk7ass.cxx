//Write a program that allows a user to enter any value from  1 to 10 and also generates random numbers. If the number entered by the user is greater than the number generated by the computer, the user Wins. Otherwise the Computer Wins

#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

int main(){
	   int n, max, computer_entry; //declare variables
	   max = 10; //set the upper bound to generate the random number
	   srand(time(0)); //make seed a function of time
	   computer_entry = (rand() % max) + 1; //store remainder in variable
	   cout << "Enter a number from 1 - 10: ";
	   cin >> n; //get user input
	   
	   //validate input n to ensure it's in the range of 1 - 10 and an integer
	   if(n > 10 || n < 1 || !(int)n){
	   	cout << "\nYou have selected an invalid number.\n";
	   }
	   else{
			cout << "\nYou pick " << n << " || " << "Computer picks " << computer_entry << "\n\n";
			if (n > computer_entry){
			cout << "You WIN! Congratulations." << endl;
			}
			else if (n == computer_entry){
				cout << "It's a TIE!" << endl;
			}
			else {
				cout << "Sorry, you LOSE!" << endl;
			}
		}
		return 0;
}