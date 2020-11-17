package models;

import java.util.Map;

/**
 * This interface defines the callback mechanic a user must define to handle update messages.
 */
@FunctionalInterface
public interface UpdateCallback {

    void sendCallback(Map<String, Update> currentUpdate);
}
