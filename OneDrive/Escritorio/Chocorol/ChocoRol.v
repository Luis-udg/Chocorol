`timescale 1ns/1ns
module MemoriaA(
	input [4:0]Dir1Lec,
	input [4:0]Dir2Lec,
	input [4:0]DirEs,
	input [31:0]DatosEscritura,
	input WE,
	output reg [31:0]Dato1,
	output reg [31:0]Dato2
);
reg [31:0] memoriaA [0:31];
initial begin
	$readmemh("datos.txt",memoriaA);
	#10;
end
 always @(*) begin
        if (WE) begin
            memoriaA[DirEs] = DatosEscritura;  // Escritura
        end
            Dato1 = memoriaA[Dir1Lec]; // Lectura de la memoria
			Dato2 = memoriaA[Dir2Lec];
    end
endmodule

module MemoriaB(
	input [4:0]Direccion,
	input [31:0]datos,
	input WE,
	output reg [31:0]Q
);
reg [31:0] memoriaB [0:31];

 always @(*) begin
        if (WE) begin
            memoriaB[Direccion] = datos;  // Escritura
        end
            Q = memoriaB[Direccion]; // Lectura de la memoria
    end
endmodule 

//Modulo ALU
module ALU(
	input [2:0]SEL,
	input [31:0]op1,
	input [31:0]op2,
	output reg [31:0]resultado,
	output zf
);
always @(*) begin
    case (SEL)
        3'b000: begin
            resultado=op1&op2;
        end
		3'b001: begin
            resultado=op1|op2;
        end
		3'b010: begin
            resultado=op1+op2;
        end
		3'b011: begin
            resultado=op1-op2;
        end
		3'b100: begin
            resultado=(op1 < op2) ? 32'b1 : 32'b0;
        end
		3'b101: begin
            resultado=~(op1|op2);
        end
        default: begin
            resultado=0;
        end
    endcase
end
assign zf= resultado==32'd0 ? 32'd1 : 32'd0;
endmodule

module ChocoRol(
	input [19:0] Instruccion,
	output [31:0]R
);
wire [31:0]c1;
wire [31:0]c2;
wire [31:0]c3;
//wire [31:0]c4;
MemoriaA A( .Dir1Lec(Instruccion[17:13]),
.Dir2Lec(Instruccion[9:5]),
.WE(Instruccion[19]),.Dato1(c1),.Dato2(c2) );

ALU alu( .SEL(Instruccion[12:10]),.op1(c1),.op2(c2),
.resultado(c3) );

MemoriaB B( .Direccion(Instruccion[4:0]),.datos(c3),.WE(Instruccion[18]),
.Q(R) );

endmodule