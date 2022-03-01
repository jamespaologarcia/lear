"""sp_gp

Revision ID: 33501a263f32
Revises: 94586877d4bc
Create Date: 2022-02-28 12:53:01.294444

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '33501a263f32'
down_revision = '94586877d4bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('businesses', sa.Column('business_start_date', sa.DateTime(timezone=True), nullable=True))
    op.add_column('businesses', sa.Column('naics_key', sa.String(length=50), nullable=True))
    op.add_column('businesses', sa.Column('naics_code', sa.String(length=10), nullable=True))
    op.add_column('businesses', sa.Column('naics_description', sa.String(length=150), nullable=True))
    op.add_column('businesses_version', sa.Column('business_start_date', sa.DateTime(timezone=True), nullable=True))
    op.add_column('businesses_version', sa.Column('naics_key', sa.String(length=50), nullable=True))
    op.add_column('businesses_version', sa.Column('naics_code', sa.String(length=10), nullable=True))
    op.add_column('businesses_version', sa.Column('naics_description', sa.String(length=150), nullable=True))
    op.add_column('parties', sa.Column('identifier', sa.String(length=10), nullable=True))
    op.add_column('parties', sa.Column('tax_id', sa.String(length=15), nullable=True))
    op.add_column('parties', sa.Column('email', sa.String(length=254), nullable=True))
    op.add_column('parties_version', sa.Column('identifier', sa.String(length=10), nullable=True))
    op.add_column('parties_version', sa.Column('tax_id', sa.String(length=15), nullable=True))
    op.add_column('parties_version', sa.Column('email', sa.String(length=254), nullable=True))

    op.execute("CREATE SEQUENCE business_identifier_sp_gp START 1000000")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('parties_version', 'email')
    op.drop_column('parties_version', 'tax_id')
    op.drop_column('parties_version', 'identifier')
    op.drop_column('parties', 'email')
    op.drop_column('parties', 'tax_id')
    op.drop_column('parties', 'identifier')
    op.drop_column('businesses_version', 'naics_description')
    op.drop_column('businesses_version', 'naics_code')
    op.drop_column('businesses_version', 'naics_key')
    op.drop_column('businesses_version', 'business_start_date')
    op.drop_column('businesses', 'naics_description')
    op.drop_column('businesses', 'naics_code')
    op.drop_column('businesses', 'naics_key')
    op.drop_column('businesses', 'business_start_date')

    op.execute("DROP SEQUENCE business_identifier_sp_gp")
    # ### end Alembic commands ###
