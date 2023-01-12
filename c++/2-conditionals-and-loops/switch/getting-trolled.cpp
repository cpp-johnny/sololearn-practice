#include <iostream>
using namespcae std;

int main() {
    int x = 3;
    switch(x) {
      case 2:
        x = 6;
      case 3:
        x = 9;
      case 4:
        x = 7;
        break;
      case 5:
        x = 8;
    }
    return 0;
}

/*
you will think the answer is 9, but the answer is actually 7! 
Why? Note: only case 4 ends with `break;` , which is required for it to be executed. 
*/
