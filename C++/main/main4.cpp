#include <iostream>
#include <string>
using namespace std;

// void Hello(){
//     cout << "Hello";
// }

// int main(){
//     Hello();
//     return 0;
// }

// void Names(string fname){
//     cout << "Hello " << fname;
// }

// int main(){
//     string name = "Bob";
//     Names(name);
//     return 0;
// }

// int Fibonacci(int n){
//     if (n<=1){
//         return n;
//     }
//     else {
//         return Fibonacci(n-1) + Fibonacci(n-2);
//     }
// }

// int main(){
//     int term;
//     cout << "Enter the number of Fibonacci Terms: ";
//     cin >> term;
//     for (int i=0; i<=term; i++){
//         cout << Fibonacci(i) << "\n";
//     }
//     return 0;
// }

// class Vehicle {
//   public:
//     string brand = "Ford";
//     void honk() {
//       cout << "Tuut, tuut! \n" ;
//     }
// };

// class Car: public Vehicle {
//   public:
//     string model = "Mustang";
// };

// int main() {
//   Car myCar;
//   myCar.honk();
//   cout << myCar.brand + " " + myCar.model;
//   return 0;
// }

// int sum(int k) {
//   if (k > 0) {
//     return k + sum(k - 1);
//   } else {
//     return 0;
//   }
// }

int main() {
  try {
  int age = 15;
  if (age >= 18) {
    cout << "Access granted - you are old enough.";
  } else {
    throw (age);
  }
}
catch (int myNum) {
  cout << "Access denied - You must be at least 18 years old.\n";
  cout << "Age is: " << myNum;
}
}

