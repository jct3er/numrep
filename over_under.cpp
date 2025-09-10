#include <iostream>
using namespace std;

int main(int argc, char* argv){
int N = 1080;

float sing_low = 1;
float sing_high = 1;
double doub_low = 1;
double doub_high = 1;

for (int i=0; i<N; i++){

  sing_low /= 2;
  sing_high *= 2;
  doub_low /= 2;
  doub_high *= 2;

  std::cout << "Loop Iteration: " << i << "\nSingle high low: " << sing_high << " " << sing_low <<  "\nDouble high low: " << doub_high << " " << doub_low << "\n" << std::endl;

 };

 std::cout << "\n\n\nStarting Integers \n\n\n" << std::endl;

 long int M = 1000;
 int int_high = 2147480000;
 int int_low = -2147480000;
 unsigned int un_high = 4294967000;

 for (int i=1; i<M; i++){

   int_high++;
   int_low--;
   un_high++;

   std::cout << "Loop Iteration: " << i << "\nInteger high low: " << int_high << " " << int_low <<  "\nUnsigned: " << un_high << "\n" << std::endl;
 };

 return 0;
};
