#include <iostream>
#include <string>
using namespace std;

// int main(){
//     int age;
//     cout << "Enter your age: ";
//     cin >> age;
//     if (age>=18){
//         cout << "You are eligible to vote";
//     } else{
//         cout << "You can't vote";
//     }
//     return 0;
// }

// int main(){
//     int time=20;
//     string result = (time<18) ? "Hi" : "Bye";
// }

// int main(){
//     int age=20;
//     string feedback = (age>=18) ? "You can vote" : "You can't vote";
//     cout << feedback;
// }

// int main(){
//     int age=2;
//     switch (age){
//     case 1:
//         cout << "Hi";
//         break;
//     case 2:
//         cout << "Hello";
//         break;
//     case 3:
//         cout << "Bye";
//         break;
//     }
// }

// int main(){
//     int age=6;
//     switch (age){
//     case 1:
//         cout << "Hi";
//         break;
//     case 2:
//         cout << "Hello";
//         break;
//     case 3:
//         cout << "Bye";
//         break;
//     default:
//         cout << "Hey there!";
//     }
// }

// int main(){
//     int x=5;
//     while (x<10){
//         cout << x << endl;
//         x++;
//     }
//     return 0;
// }

// int main(){
//     int age;
//     cout << "Enter your age: ";
//     cin >> age;
//     if (age>10){
//         cout << "You are not a decade years old";
//     } else if (age<10){
//         cout << "You are not a decade years old";
//     } else{
//         cout << "You are a decade years old";
//     }
//     return 0;
// }

// int main(){
//     for (int j = 0; j<10; j++){
//         if (j==4){
//             break;
//         }
//         else{
//             cout << j << "\n";
//         }
//     }
//     return 0;
// }

// int main(){
//     string languages[6] = {"HTML", "CSS", "C++", "C", "Java", "Python"};
//     for (int i=0; i<6; i++){
//         cout << languages[i] << "\n";
//     }
//     return 0;
// }

// int main(){
//     int length = 4;
//     int numbers[length] = {30,20,45,36};
//     for (int i=0; i<length; i++){
//         cout << numbers[i] << "\n";
//     }
//     return 0;
// }

// int main(){
//     int numbers[4] = {30,20,45,36};
//     for (int i : numbers){       type var : array
//         cout << i << "\n";
//     }
//     return 0;
// }

// int main(){
//     int classname[6] = {10,12,45,554,22,29};
//     for (int i : classname){       
//         cout << i << "\n";
//     }
//     return 0;
// }

// int main(){
//     int classname[6] = {10,12,45,554,22,29};
//     cout << sizeof(classname);
//     return 0;
// }

// int main(){
//     int myfriends[6] = {2,7,4,30,23,44};
//     cout << sizeof(myfriends);
//     return 0;
// }

// int main(){
//     int myfriends[6] = {2,7,4,30,23,44};
//     int getArrayLength = sizeof(myfriends)/sizeof(int);
//     cout << getArrayLength;
//     return 0;
// }

// struct Zephyr{
//     int intName;
//     string stringName;
// };

// int main(){
//     Zephyr z1;
//     z1.intName = 20;
//     z1.stringName = "C++";

//     Zephyr z2;
//     z1.intName = 50;
//     z1.stringName = "C";

//     cout << "IntegerName" << " " << "StringName" << "\n"; 
//     cout << z1.intName << " " << z1.stringName << "\n";
//     cout << z2.intName << " " << z2.stringName << "\n";

//     return 0;
// }


// int main(){
//     struct {
//         int Marks;
//         string Languages;
//     } List1, List2;

//     List1.Marks = 25;
//     List1.Languages = "HTML";

//     List2.Marks = 30;
//     List2.Languages = "CSS";

//     cout << List1.Marks << " " << List1.Languages << "\n";
//     cout << List2.Marks << " " << List2.Languages << "\n";

//     return 0;
// }

// There are 3 types of conditions in c++
// if condition, else if condition, else condition


// int main(){
//     if (condition){
//         <statement>;
//     }
//     return 0;
// }

// int main(){
//     int num=3;
//     switch (age){
//     case 1:
//         cout << "Hi";
//         break;
//     case 2:
//         cout << "Hello";
//         break;
//     case 3:
//         cout << "Bye";
//         break;
//     default:
//         cout << "Hey there!";
//     }
// }

// Difference between a while and do while is that. 
// In do while, the loop will execute once even before checking the condition, 
// whereas in a while loop, the loop executes if the condition is true

// Break statement terminates the entire loop. 
// Continue statement only stops/skips the current iteration of the loop.

// int main(){
//     for (int i=10;i<20;i++){
//         cout << i << "\n";
//     }
//     return 0;
// }

// Arrays are used to store data in a single variable that is easy to access and handle
// Example: We can store Matrice values in Array

// int main(){
//     string arrayName[6] = {"html", "css", "java", "c++", "python", "c"};

//     for (string i : arrayName){
//         cout << i << "\n";
//     }
//     return 0;
// }

// Structures are a way to store multiple related variables into one variable
// Example: 
// int main(){
//     struct {
//         int Marks;
//         string Languages;
//     } List1;

//     List1.Marks = 25;
//     List1.Languages = "HTML";

//     cout << List1.Marks << " " << List1.Languages << "\n";

//     return 0;
// }

// int main(){
//     string day = "Friday";
//     if (day=="Monday"){
//         cout << "It is Monday!";
//     }
//     else if (day!="Monday"){
//         cout << "It's not Monday";
//     }
//     else {
//         cout << "Invalid Day";
//     }
//     return 0;
// }