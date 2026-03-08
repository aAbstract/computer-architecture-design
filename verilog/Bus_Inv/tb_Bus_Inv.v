`timescale 1ns/1ns

module tb_Bus_Inv;

reg [7:0] tb_In1;
wire [7:0] tb_Out1;

Bus_Inv dut (
    .In1(tb_In1),
    .Out1(tb_Out1)
);

initial begin
    $dumpfile("tb_Bus_Inv.vcd");
    $dumpvars(0, tb_Bus_Inv);
    $monitor("Time=%0t | In1=%b | Out1=%b", $time, tb_In1, tb_Out1);

    tb_In1 = 8'b0000_0000; #10;
    tb_In1 = 8'b1111_1111; #10;
    tb_In1 = 8'b1010_1010; #10;
    tb_In1 = 8'b0101_0101; #10;

    $finish;
end

endmodule
