// normal for loop
#include <iostream>
using namespace std;

int main() {
    for(int i=1;i<=5;i++) {
        cout << i << endl;
    }
}

// output: 1, 2, 3, 4, 5




// for loop with `break;` --> exits the loop when condition is met
#include <iostream>
using namespace std;

int main() {
    for(int i=0;i<10;i++) {
        if(i==5) {
            break;
        }
        cout << i << endl;
    }
}

// output: 0,1,2,3,4



// for loop with `continue;` -->  The continue statement skips the current loop iteration and continues with the next one.
#include <iostream>
using namespace std;

int main() {
    for(int i=0;i<10;i++) {
        if(i==5) {
            continue;
        }
        cout << i << endl;
    }
}

// output: 0,1,2,3,4,6,7,8,9


//combination
#include <iostream>
using namespace std;

int main() {
    for(int x=1;x<10;x++) {
      if(x == 2) {
        continue; 
      }
      if(x == 5) {
        break;
      }
      cout << x << endl;
    }
}

// output: 1, 3, 4
