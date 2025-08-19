#pragma once

#include <chrono>
#include <string>

namespace library {
class Update {
public:
    std::string name;
    std::string version;
    std::chrono::time_point<std::chrono::system_clock> processed;
    std::string data;
};

}