# include <iostream>
using namespace std;
# define MAX 4
int stack_array[MAX];
int top= -1;

// INSERTION IN STACK IN C++ 

void push(int data){
    if (top==MAX -1){
        cout<< ("stack overflow");
        return;
    }
    top = top + 1;
    stack_array[top] = data;
    cout<<stack_array<<endl;
}
void pop(int data){
    if (top== MAX)
}

int main(){
    cout<<"mahesh ravaji";
    push(1);
    push(2);
    push(3);
    push(14);
    push(22);


}

