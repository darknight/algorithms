#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
	stack<int> s1;
	stack<int> s2;
	int n, k;
	string op;
	cin>>n;
	while(cin>>op) {
		//cout<<op<<endl;
		if(op == "PUSH") {
			cin>>k;
			//cout<<k<<endl;
			s1.push(k);
		}
		if(op == "POP") {
			if(s2.empty()) {
				while(!s1.empty()) {
					s2.push(s1.top());
					s1.pop();
				}
				if(s2.empty()) {
					cout<<-1<<endl;
					continue;
				}
			}
			cout<<s2.top()<<endl;
			s2.pop();
		}
	}
	return 0;
}
