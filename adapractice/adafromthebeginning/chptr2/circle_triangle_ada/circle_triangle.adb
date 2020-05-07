with Ada.Text_Io;
use Ada.Text_Io;

package body circle_triangle is
    procedure Draw_Triangle is
    begin
        Put_Line("       **       ");
        Put_Line("      ****      ");
        Put_Line("    ********    ");
        Put_Line("  ************  ");
        Put_Line("****************");
    end Draw_Triangle;
    procedure Draw_Circle is
    begin
        Put_Line("      ***       ");
        Put_Line("    ***  ***    ");
        Put_Line("  ***      ***  ");
        Put_Line("***          ***");
        Put_Line("***          ***");
        Put_Line("  ***     ***   ");
        Put_Line("    *** ***     ");
        Put_Line("      ***       ");
    end Draw_Circle;
end circle_triangle;
