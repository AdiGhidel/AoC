#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <filesystem>
#include <string>
#include <numeric>
#include <cmath>

std::vector<int> readFile() {
    std::vector<int> in;
    /* Read input */

    if (!std::filesystem::exists("input.txt"))
    {
        std::cout << "input file does not exist" << std::endl;
        exit(1);
    }

    std::ifstream input("input.txt");

    /* Read data */

    while (!input.eof())
    {
        int val;
        std::string line;

        std::getline(input, line);
        std::replace(line.begin(), line.end(), ',', ' ');
        std::istringstream linestream(line);

        while (linestream >> val)
        {
            in.push_back(val);
        }
    }
    return in;
}

int main()
{
    std::vector<int> in = {};
    in = readFile();
    return 0;
}