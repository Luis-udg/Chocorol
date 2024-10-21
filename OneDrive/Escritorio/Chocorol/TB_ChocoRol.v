`timescale 1ns/1ns

module TB_ChocoRol();
reg [19:0] instruccionTb;
wire [19:0]resultadoTb;

ChocoRol chocorol2( .Instruccion(instruccionTb),.R(resultadoTb) );

initial begin
	instruccionTb=20'b01001000100000000011;
	#100;
	instruccionTb=20'b01001110110010100000;
	#100;
	instruccionTb=20'b00000001110001000000; 
	#100;
	instruccionTb=20'b00000001110001000011; 
	#100;
	$stop;
end
endmodule
