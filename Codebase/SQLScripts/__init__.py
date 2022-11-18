DefaultPriorityColors={
    1:16399941,
    2:16070549,
    3:8069048,
    4:9201120,
    5:2287801,
    6:5177211,
    7:432432,
    8:13419293,
    9:16729344,
    10:16249827,
}
ScriptSetDefaultColors=f"""
-- The Following Commands sets the Default Colors again
BEGIN;
-- DELETE ALL THE VALUES IN THE TABLE
DELETE FROM prcolors;

-- Now Insert the Values into the table 
INSERT INTO prcolors (level,clrvalue) VALUES {f'{list(DefaultPriorityColors.items())}'.strip('[]')} ;
END;
"""