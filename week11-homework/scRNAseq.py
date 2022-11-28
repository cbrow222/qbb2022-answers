#!/usr/bin/env python

import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

# sc.tl.pca(adata, svd_solver='arpack') #run PCA on unfiltered data
# sc.pl.pca(adata, save='unfiltered.png') #plot it as a scatterplot

sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=False)

sc.tl.pca(adata, svd_solver='arpack') #run PCA on filtered data
# sc.pl.pca(adata, save='filtered.png') #plot it as a scatterplot

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.leiden(adata)

# sc.tl.umap(adata, maxiter=1000)
# sc.pl.umap(adata, color='leiden', save='leiden.png')

sc.tl.tsne(adata)
# sc.pl.tsne(adata, color='leiden', save='leiden.png')

sc.tl.rank_genes_groups(adata, 'leiden', method='t-test')
# sc.pl.rank_genes_groups(adata, save='ttest.png')

# sc.tl.rank_genes_groups(adata, 'leiden', method='logreg')
# sc.pl.rank_genes_groups(adata, save='logreg.png')

# genes=adata.var.index
# for i in range(0, len(genes), 7):
#     sc.pl.tsne(adata, color=genes[i], save='gene[i].png')
    
# Marker_genes=['Prox1', 'Rgs5', 'Egfl7', 'C1qc', 'Ndnf', 'Hba-a2']
#
# for i in range(len(Marker_genes)):
#     sc.pl.tsne(adata, color=Marker_genes[i], save=f"{Marker_genes[i]}.png")
#
# sc.pl.tsne(adata, color=Marker_genes, save="Marker_gene.png")
#
# regions=['hippocampus', 'pericytes', 'endothelial', 'macrophages', 'neurons', 'SNC']
marker_genes_dict = {'hippocampus':['Prox1'], 'pericytes':['Rgs5'], 'endothelial':['Egf17'], 'macrophages':['C1qc'], 'neurons':['Ndnf'], 'SNC':['Hba-a2']}
#sc.pl.dotplot(adata, marker_genes_dict, 'clusters', dendrogram=True)
cluster2annotation={'13':'hippocampus', '23':'pericytes', '20':'endothelial', '24':'macrophages', '21':'neurons', '15':'SNC'}

adata.obs['cell type'] = adata.obs['leiden'].map(cluster2annotation).astype('category')

sc.pl.tsne(adata, color='cell type', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2, save="Final_plot.png")