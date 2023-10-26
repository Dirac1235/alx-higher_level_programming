//write a c++ program to find the factorial of a number	
#include<iostream>
using namespace std;
int main(){
	
	int n;
	cout<<"Enter the number"<<endl;
	cin>>n;
	int fact=1;
	for(int i=1;i<=n;i++){
		fact=fact*i;
	}
	cout<<"Factorial of "<<n<<" is "<<fact<<endl;
	return 0;
	
}