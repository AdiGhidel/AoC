#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <filesystem>
#include <string>
#include <numeric>
#include <cmath>

int median(std::vector<int> v)
{
    size_t n = v.size() / 2;
    std::sort(v.begin(), v.end());
    return v[n];
}

int mean(std::vector<int> v)
{
    size_t len = v.size();
    size_t sum = 0;
    for (auto &el : v)
    {
        sum += el;
    }
    return sum / len;
}

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
    std::vector<int> crabs = {};
    long int sum = 0, m = 0;

    crabs = readFile();

    // 1
    m = median(crabs);
    sum = 0;

    for (auto c : crabs)
    {
        sum += abs(c - m);
    }

    std::cout << "Part1: " << sum << std::endl;

    // 2
    m = mean(crabs);
    sum = 0;

    for (auto c : crabs)
    {
        int cost = abs(c - m);
        sum += cost * (cost + 1) / 2;
    }

    std::cout << "Part2: " << sum << std::endl;

    return 0;
}