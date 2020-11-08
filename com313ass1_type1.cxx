//Type 1
#include <iostream>
using namespace std;

//Class declaration with required attributes
class Citrus {
	public:
	string name, color, flavour;
};

//Main function
int main() {
	Citrus fruit1; //Object 1
	Citrus fruit2; //Object 2
	
	//Object Attributes
	fruit1.name = "Orange";
	fruit1.color = "orange";
	fruit1.flavour = "sweet";
	fruit2.name = "Lemon";
	fruit2.color = "yellow";
	fruit2.flavour = "sour";
	
	//Output
	cout << fruit1.name << " is a " << fruit1.flavour << " citrus fruit with an " << fruit1.color << " color." << endl;
	cout << "\n" << fruit2.name << " is a " << fruit2.flavour << " citrus fruit with a " << fruit2.color << " color." << endl;
	return 0;
}