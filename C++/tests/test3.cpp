#include <iostream>
using namespace std;

int main() {
    int integer;
    cout << "Enter a number: ";
    cin >> integer;

    while (integer != 1) {
        if (integer % 2 == 0) {
            integer /= 2;
            cout << integer << endl;
        }
        else if (integer % 2 != 0) {
            integer = 3 * integer + 1;
            cout << integer << endl;
        }
        else {
            cout << "Unknown Number" << endl;
        }
    }

    return 0;
}