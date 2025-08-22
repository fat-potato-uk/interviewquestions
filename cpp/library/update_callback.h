#pragma once

#include <map>
#include <string>

#include "library/update.h"

namespace library {

class UpdateCallback {
public:
    virtual ~UpdateCallback() = default;

    virtual void sendCallback(const std::map<std::string, Update> & currentUpdate) =  0;
};

}