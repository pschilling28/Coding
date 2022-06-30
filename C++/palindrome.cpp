#include <iostream>

bool is_palindrome(std::string text) {
    int count = 0; 
    for (int i = 0; i < text.size(); i++) {
        if (text[i] == text[text.size() - 1 - i]) {
            count++;
        }
    }
    if (count == text.size()) {
      return true;
    }
    return false;
}

int main() {

  std::cout << is_palindrome("madam") << "\n";
  std::cout << is_palindrome("ada") << "\n";
  std::cout << is_palindrome("lovelace") << "\n";
  std::cout << is_palindrome("boob") << "\n";
  std::cout << is_palindrome("QWERTYUIOPPOIUYTREWQ") << "\n";
  
}