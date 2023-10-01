CREATE TABLE `TB_STG_MAPA_SUPORTE` (
	`CODIGO` BIGINT AUTO_INCREMENT,
    `Posição / TAG` nvarchar(255) NOT NULL,
    `Identificação` nvarchar(255) NOT NULL,
    `Prog Fab` nvarchar(255) NOT NULL,
    `Desenho Suporte` nvarchar(255),
    `Tipo de Suporte` nvarchar(255),
    `Tipo Estrutura` nvarchar(255),
    `Linha` nvarchar(255),
    `Isométrico` nvarchar(255),
    `Spool` nvarchar(255),
    `Qtde` float,
    `Peso (Kg)` float,
    `Número Romaneio` nvarchar(255),
    `Data Romaneio` datetime,
    `Localização` nvarchar(255),
    `Status` nvarchar(255),
    `Observação` nvarchar(255),
    `Dimensão H` float,
    `Dimensão L` float,
    `Dimensão M` float,
    `Dimensão N` float,
    `Data Cadastro` datetime,
    `ID_SISTEMA` float,
	PRIMARY KEY (CODIGO)
)