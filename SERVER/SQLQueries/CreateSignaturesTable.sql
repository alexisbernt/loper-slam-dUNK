GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- Note:
-- signatureRow = SignaturesTable(PrimaryKey=signature, InstallCount=0, InstallLimit=0, UnlimitedInstalls=unlimitedInstalls)

DROP TABLE IF EXISTS [dbo].Signatures
if not EXISTS(select * from sys.tables t join sys.schemas s on (t.schema_id = s.schema_id) where s.name = 'dbo' and t.name = 'Signatures')
BEGIN
CREATE TABLE [dbo].[Signatures](
		[Signature] nvarchar(255) UNIQUE NOT NULL,
		InstallCount int NOT NULL,
		InstallLimit int NOT NULL,
		UnlimitedInstalls BIT NOT NULL,
		PRIMARY KEY ([Signature]),
	) ON [PRIMARY]
END
GO