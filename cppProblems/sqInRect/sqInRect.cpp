#include <vector>
#include <iostream>

class SqInRect
{
public:
    static std::vector<int> sqInRect(int lng, int wdth)
    {
        int totalLength = lng * wdth;
        const int starter = lng > wdth ? wdth : wdth > lng ? lng
                                                           : lng;
        std::vector<int> sides;
        if (lng == wdth)
        {
            return sides;
        }
        int i = starter;
        while (totalLength > 0)
        {
            const int squared = i * i;
            if (squared <= totalLength && i <= lng && i <= wdth)
            {
                totalLength -= squared;
                sides.push_back(i);
                int newLen = lng;
                int newWdth = wdth;
                if (lng > wdth)
                {
                    newLen = lng - i;
                }
                else if (wdth > lng)
                {
                    newWdth = wdth - i;
                }
                lng = newLen;
                wdth = newWdth;
                i = lng > wdth ? wdth : wdth > lng ? lng
                                                   : wdth;
                continue;
            }
            i--;
        }
        return sides;
    }
};

int main(void)
{
    SqInRect::sqInRect(5, 3);
}