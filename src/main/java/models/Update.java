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
    private String name;

    @NonNull
    private String version;

    @NonNull
    private ZonedDateTime processed;

    @NonNull
    private String data;
}
