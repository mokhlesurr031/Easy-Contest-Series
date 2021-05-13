// C++ program to demonstrate vector of strings using
#include <iostream>
#include <vector>
#include <string>

int main()
{
    // Declaring Vector of String type
    // Values can be added here using initializer-list syntax
    std::vector<std::string> colour {"Blue", "Red", "Orange"};

    // Strings can be added at any time with push_back
    colour.push_back("Yellow");
    std::cout<<colour.size();

    // Print Strings stored in Vector
    for (int i = 0; i < colour.size(); i++)
        std::cout << colour[i] << "\n";


}
