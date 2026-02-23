print("Running Supplier Segmentation Pipeline\n")

print("Step 1: Data loading and preprocessing")
exec(open("scripts/01_data_loading_and_preprocessing.py").read())

print("\nStep 2: Exploratory Data Analysis")
exec(open("scripts/02_exploratory_data_analysis.py").read())

print("\nStep 3: Supplier Segmentation")
exec(open("scripts/03_supplier_segmentation.py").read())

print("\nPipeline completed successfully")
