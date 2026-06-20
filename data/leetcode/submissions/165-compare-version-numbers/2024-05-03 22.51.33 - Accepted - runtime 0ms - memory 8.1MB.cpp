class Solution {
public:
    int compareVersion(string version1, string version2) {

        int curr1, curr2;
        int end1, end2;
        while (!version1.empty() && !version2.empty())
        {
            end1 = version1.find('.');
            end2 = version2.find('.');

            end1 = end1 == -1 ? version1.length() : end1;
            end2 = end2 == -1 ? version2.length() : end2;

            curr1 = std::stoi(version1.substr(0, end1));
            curr2 = std::stoi(version2.substr(0, end2));

            if (curr1 < curr2) return -1;
            if (curr2 < curr1) return 1;

            version1 = version1.substr(std::min((int)version1.size(), end1 + 1));
            version2 = version2.substr(std::min((int)version2.size(), end2 + 1));
        }

        while (!version1.empty())
        {
            end1 = version1.find('.');
            end1 = end1 == -1 ? version1.length() : end1;

            curr1 = std::stoi(version1.substr(0, end1));
            if (curr1 > 0) return 1;

            version1 = version1.substr(std::min((int)version1.size(), end1 + 1));
        }
        while (!version2.empty())
        {

            end2 = version2.find('.');
            end2 = end2 == -1 ? version2.length() : end2;

            curr2 = std::stoi(version2.substr(0, end2));

            if (curr2 > 0) return -1;

            version2 = version2.substr(std::min((int)version2.size(), end2 + 1));
        }

        return 0;
    }
};