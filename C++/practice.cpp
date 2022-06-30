#include <iostream>
using namespace std;

int main(void) {
    
//Module 2 Exam Code
    /*2Q1
        int i = 1, j = i++, k = --i;
        if(i > 0) {
            j++;
            k++;
        }
        else {
            k++;
            i++;
        }
        if(k == 0) {
            i++;
            j++;
        }
        else {
            if(k > 0)
                k--;
            else
                k++;
            i++;
        }
        std::cout << i * j * k;*/
    /*2Q2 double holds 15-17 digits accurately so big are kept, but small are chopped
        double big = 1e15;
        double small = 1e-15;
    
        std::cout << std::fixed << big + small;*/
    /*2Q3
        int i = 5, j = 0;
            while(i > 0) {
                i--;
                j++;
            }
            cout << j;*/
    /*2Q4 careful on this one ">=" runs it a fourth time.
        int i = 3, j = 0;
                do {
                    i--;
                    j++;
                } while(i >= 0);
                cout << j;*/
    /*2Q5
        for(float val = -10.0; val < 100.0; val = -val * 2)
            cout << "*";*/   
    /*2Q6
        for(float val = -10.0; val < 100.0; val = -val * 2) {
                    if(val < 0 && -val >= 40)
                        break;
                    cout << "*";}*/  
    /*2Q7 left a means *(2^a)
        int a = 3;
                switch(a << a) {
                case 8 : a++;
                case 4 : a++;
                case 2 : break;
                case 24 : a--;
                }
                cout << a;*/  
    /*2Q8
        int t[] = { 5, 4, 3, 2, 1 }, i;
                for(i = t[4]; i < t[0]; i++)
                    t[i - 1] = -t[3];
                cout << i;*/
    /*2Q9
        struct str {
            int t[3];
            char s[3];
        };
        str a = { 1, 2, 3, 'a', 'b', 'c' };
        str b = { 5, 6, 7, 'x', 'y', 'z' };
        cout << char(b.s[0] + a.t[0]) << int(a.s[2] - a.s[0]) << int(b.s[2] - b.s[1]);*/
    /*Q10 figure this one out! syntactically confusing. = to: str t[2] ={ { { {0, 2}, {4, 6} } }, { { {1, 3}, {5, 7} } } };

            struct sct {
                int t[2];
            };
        
            struct str {
                sct t[2];
            };
        
            str t[2] = { {0, 2, 4, 6}, {1, 3, 5, 7} };
            
            cout << t[1].t[0].t[1] << t[0].t[1].t[0];*/

//3.1.22 compiler mem usage code
    /*cout << "This computing environment uses:" << endl;
    cout << sizeof(char) << " bytes for chars" << endl;
    cout << sizeof(short int) << " bytes for shorts" << endl;
    cout << sizeof(int) << " bytes for ints" << endl;
    cout << sizeof(long int) << " bytes for longs" << endl;
    cout << sizeof(float) << " bytes for floats"  << endl;
    cout << sizeof(double) << " bytes for doubles"  << endl;
    cout << sizeof(bool) << " byte for bools" << endl;
    cout << sizeof(int *) << " bytes for pointers" << endl;*/
 
//3 practice quiz

    /*study this one more -- answer is -1
        int t[4] = {8, 4, 2, 1};
        int *p1 = t + 2, *p2 = p1 - 1;
        p1++;
        cout << *p1 - t[p1 - p2] << endl;*/
    /*study this one more -- answer is **
            /*copy/paste outside of main
            int fun(int p) {
                int cnt = 0;
                for(p = 2 * p; p > 0; p >>= 2)
                    cnt ++;
                return cnt;
            }

            void foon(int p) {
                for(int cnt = fun(p); cnt > 0; cnt--)
                    cout << "*";
            }*/
        /*execute in main
        foon(2);
        cout << endl;*/
    /*study this one more -- answer is 8
        /*copy/paste outside of main
        int fun1(int p) {
            ++p;
            return p++;
        }
        int fun2(int &p) {
            ++p;
            return p++;
        }*/
        /*execute in main
        int a = 1, b, c;
        b = fun1(a);
        c = fun2(b);
        cout << a + b + c << endl;*/
    /*study this one more -- answer is 4
        /*copy/paste outside of main
        int *fun(void) {
            return new int[2];
        }
        int fun(int *p) {
            delete [] p;
            return 0;
        }
        void fun(int *p, int q) {
            p[q] *= 2;
        }
        void fun(int *p, int q, int r) {
            p[q] = r;
        }*/
        /*execute in main
        int *v = fun();
        fun(v,0,1);
        fun(v,1,2);
        fun(v,0);
        cout << v[1] + v[0] << endl;
        fun(v);*/
    /*study this one more -- answer is yza
        /*copy/paste outside of main
        char f1(char c) {
            return c == 'z' ? 'a' : c + 1;
        }
        char f2(char &c) {
            c = f1(c);
            return c;
        }*/
        /*execute in main
        char x = 'x';
        cout << f2(x);
        cout << f2(x);
        cout << f2(x) << endl;*/

    return 0;
}
