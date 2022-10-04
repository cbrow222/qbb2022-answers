#QBB2022-Week4 Homework Exercises Solutions

2. plink --vcf gwas_data/genotypes.vcf --pca 10 'tabs'
3. plink --vcf gwas_data/genotypes.vcf --pca 10 'tabs' --freq
4. plink --vcf gwas_data/genotypes.vcf --pheno gwas_data/CB1908_IC50.txt --linear --covar plink.eigenvec --allow-no-sex --hide-covar
plink --vcf gwas_data/genotypes.vcf --pheno gwas_data/GS451_IC50.txt --linear --covar plink.eigenvec --allow-no-sex --hide-covar

GS451 top SNP is rs7257475:
	Potential gene: ZNF826-a zinc finger protein
CB1908 top SNP is rs10876043:
	Potential gene:Homo sapiens disco interacting protein 2 homolog B (DIP2B)
The genome used could probably be found in the github where the GWAS data was from.