-- -----------------------------------------------------
-- Schema biblioGest
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `biblioGest` DEFAULT CHARACTER SET utf8 ;
USE `biblioGest` ;

-- -----------------------------------------------------
-- Table `biblioGest`.`cargo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`cargo` (
  `idcargo` INT NOT NULL auto_increment,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idcargo`));

-- -----------------------------------------------------
-- Table `biblioGest`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Funcionario` (
  `cpf` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `rg` VARCHAR(45) NOT NULL,
  `foto` BLOB NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `cargo_idcargo` INT NOT NULL,
  PRIMARY KEY (`cpf`),
    FOREIGN KEY (`cargo_idcargo`)
    REFERENCES `biblioGest`.`cargo` (`idcargo`));



-- -----------------------------------------------------
-- Table `biblioGest`.`Autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Autor` (
  `idAutor` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idAutor`));


-- -----------------------------------------------------
-- Table `biblioGest`.`Editora`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Editora` (
  `idEditora` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEditora`));



-- -----------------------------------------------------
-- Table `biblioGest`.`Classificacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Classificacao` (
  `idClassificacao` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idClassificacao`));


-- -----------------------------------------------------
-- Table `biblioGest`.`Secao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Secao` (
  `idSecao` INT NOT NULL auto_increment,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idSecao`));


-- -----------------------------------------------------
-- Table `biblioGest`.`Estado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Estado` (
  `idEstado` INT NOT NULL auto_increment,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEstado`));

-- -----------------------------------------------------
-- Table `biblioGest`.`Livro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Livro` (
  `registro` INT NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `paginas` INT NOT NULL,
  `edicao` INT NOT NULL,
  `dataLancamento` DATE NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `Funcionario_cpf` INT NOT NULL,
  `Autor_idAutor` INT NOT NULL,
  `Editora_idEditora` INT NOT NULL,
  `Classificacao_idClassificacao` INT NOT NULL,
  `Secao_idSecao` INT NOT NULL,
  `Estado_idEstado` INT NOT NULL,
    PRIMARY KEY (`registro`),
    FOREIGN KEY (`Funcionario_cpf`) REFERENCES `biblioGest`.`Funcionario` (`cpf`),
    FOREIGN KEY (`Autor_idAutor`) REFERENCES `biblioGest`.`Autor` (`idAutor`),
    FOREIGN KEY (`Editora_idEditora`) REFERENCES `biblioGest`.`Editora` (`idEditora`),
    FOREIGN KEY (`Classificacao_idClassificacao`) REFERENCES `biblioGest`.`Classificacao` (`idClassificacao`),
    FOREIGN KEY (`Secao_idSecao`) REFERENCES `biblioGest`.`Secao` (`idSecao`),
    FOREIGN KEY (`Estado_idEstado`) REFERENCES `biblioGest`.`Estado` (`idEstado`)
);


-- -----------------------------------------------------
-- Table `biblioGest`.`tipoPeriodico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`tipoPeriodico` (
  `idtipoRevista` INT NOT NULL auto_increment,
  `Nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtipoRevista`));

-- -----------------------------------------------------
-- Table `biblioGest`.`Periodico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Periodico` (
  `registro` INT NOT NULL,
  `titulo` VARCHAR(200) NOT NULL,
  `numero` INT NOT NULL,
  `tipoPeriodico_idtipoRevista` INT NOT NULL,
  `Funcionario_cpf` INT NOT NULL,
  `Autor_idAutor` INT NOT NULL,
  `Secao_idSecao` INT NOT NULL,
  `Editora_idEditora` INT NOT NULL,
PRIMARY KEY (`registro`),
FOREIGN KEY (`tipoPeriodico_idtipoRevista`) REFERENCES `biblioGest`.`tipoPeriodico` (`idtipoRevista`),
FOREIGN KEY (`Funcionario_cpf`) REFERENCES `biblioGest`.`Funcionario` (`cpf`),
FOREIGN KEY (`Autor_idAutor`) REFERENCES `biblioGest`.`Autor` (`idAutor`),
FOREIGN KEY (`Secao_idSecao`) REFERENCES `biblioGest`.`Secao` (`idSecao`),
FOREIGN KEY (`Editora_idEditora`) REFERENCES `biblioGest`.`Editora` (`idEditora`));


-- -----------------------------------------------------
-- Table `biblioGest`.`Produtora`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Produtora` (
  `idProdutora` INT NOT NULL auto_increment,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idProdutora`));


-- -----------------------------------------------------
-- Table `biblioGest`.`Multimidia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Multimidia` (
  `registro` INT NOT NULL,
  `data` DATE NOT NULL,
  `titulo` VARCHAR(45) NOT NULL,
  `subtitulo` VARCHAR(45) NULL,
  `Produtora_idProdutora` INT NOT NULL,
  `Funcionario_cpf` INT NOT NULL,
  PRIMARY KEY (`registro`),
    FOREIGN KEY (`Produtora_idProdutora`) REFERENCES `biblioGest`.`Produtora` (`idProdutora`),
FOREIGN KEY (`Funcionario_cpf`) REFERENCES `biblioGest`.`Funcionario` (`cpf`));

-- -----------------------------------------------------
-- Table `biblioGest`.`Leitor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Leitor` (
  `rg` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `profissao` VARCHAR(45) NOT NULL,
  `instituicao` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `endereco` VARCHAR(45) NOT NULL,
  `Funcionario_cpf` INT NOT NULL,
  `foto` BLOB NULL,
  PRIMARY KEY (`rg`),
FOREIGN KEY (`Funcionario_cpf`) REFERENCES `biblioGest`.`Funcionario` (`cpf`)
);


-- -----------------------------------------------------
-- Table `biblioGest`.`Emprestimo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`Emprestimo` (
  `idEmprestimo` INT not null auto_increment,
  `Justificativa` VARCHAR(45) NULL,
  `Leitor_rg` INT NOT NULL,
  `Periodico_registro` INT NULL,
  `Livro_registro` INT NULL,
  `status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idEmprestimo`),
  FOREIGN KEY (`Leitor_rg`) REFERENCES `biblioGest`.`Leitor` (`rg`),
	FOREIGN KEY (`Periodico_registro`) REFERENCES `biblioGest`.`Periodico` (`registro`),
    FOREIGN KEY (`Livro_registro`) REFERENCES `biblioGest`.`Livro` (`registro`)
);


-- -----------------------------------------------------
-- Table `biblioGest`.`hemeroteca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `biblioGest`.`hemeroteca` (
  `registro` INT NOT NULL,
  `assunto` VARCHAR(200) NOT NULL,
  `fornecedor` VARCHAR(100) NULL,
  `obs` VARCHAR(50) NULL,
  `Funcionario_cpf` INT NOT NULL,
  PRIMARY KEY (`registro`),
  FOREIGN KEY (`Funcionario_cpf`) REFERENCES `biblioGest`.`Funcionario` (`cpf`));

