// An array needs to be declared like a variable, with the type of the items it will hold.
// example:

double prices[5];

// example:
// declare an array called `users` of type `string` which can hold 8 items
string users[8];

// After declaring the array, we can access the items using their position, also called the index.
// Let's set the item with the index 3 to the value 29.99:
prices[3] = 29.99;

// what about the first item? note: [0] is first item!
price[0] = 29.99;

// this will output 29.99
#include <iostream>
using namespace std;

int main() {
    double prices[8];
    prices[3] = 29.99;
    
    cout << prices[3];
}


// this will outpu 15525
#include <iostream>
using namespace std;

int main() {
    int x[8];
    x[3] = 1234;
    x[2] = 9847;
    x[0] = 9847;
    x[7] = 8648367453754;
    
    cout << x[3] + x[7] + x[0];
}


// If you already know what values to store in the array, instead of assigning them one by one, you can use the following syntax:
double prices[] = {5.99, 3.2, 9.99, 29.99};


// this will output 9.99
#include <iostream>
using namespace std;

int main() {
    double prices[] = {5.99, 3.2, 9.99, 29.99};

    cout << prices[2];
}






