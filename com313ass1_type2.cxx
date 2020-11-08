//Type 2
#include <iostream>
using namespace std;

//Class declaration with required attributes
class carType {
	public:
	string type, brand, model;
};

//Main function
int main() {
	carType sedan; //Object 1
	carType coupe; //Object 2
	
	//Object Attributes
	sedan.type = "Sedan";
	sedan.brand = "Toyota";
	sedan.model = "Corolla";
	coupe.type = "Coupe";
	coupe.brand = "Audi";
	coupe.model = "A5";
	
	//Output
	cout << "A " << sedan.brand << " " << sedan.model << " is a " << sedan.type << "." << endl;
	cout << "\nAn " << coupe.brand << " " << coupe.model << " is a " << coupe.type << "." << endl;
	return 0;
}