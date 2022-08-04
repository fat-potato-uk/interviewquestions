package models;

import lombok.NonNull;
import lombok.Value;

import java.time.ZonedDateTime;

/**
 * A class representing the update received.
 */
@Value
public class Update {
    @NonNull
    String name;

    @NonNull
    String version;

    @NonNull
    ZonedDateTime processed;

    @NonNull
    String data;
}
