# project meta begin {
class TMetaProject(base):
    __tablename__ = "t_meta_project"
    id = x
    name = x
    update_at = x
    update_by = x
    manifest_repo = x
    manifest_branch = x
    manifest_name = x
    retired = x


class TMetaModule(Base):
    """
    Subset of all modules.
    """
    __tablename__ = "t_meta_module"
    id = x
    name = Column()
    project_id = relationship
    labels = Column()


class TMetaModuleHier(Base):
    """
    Only module name. NOT instance name!
    """
    __tablename__ = "t_meta_module_hier"
    id = x
    xpath = x
    children = x
    father = Column()


# class TMetaInstance
# class TMetaInstanceHier


class TMetaClockDomain(Base):
    __tablename__ = "t_meta_clock_domain"
    id = Column()
    name = Column()
    project_id = relationship
# project meta end }


# * waive related begin {
class TWaives(Base):
    __tablename__ = "t_waives"
    id = x
    from_clk = x    # clk port
    to_clk = x
    from_module = relationship
    to_module = relationship
    from_clk_domain = relationship
    to_clk_domain = relationship
    update_at = x
    update_by = x
    update_repo = x
    update_branch = x
    update_revision = x


class TWaiveGroups(Base):
    __tablename__ = "t_waive_groups"
    id = x
    name = Column()
    wildcard = x
    update_at = x
    update_by = x
    update_repo = x
    update_branch = x
    update_revision = x


class TValidWaiveLabels(Base):
    __tablename__ = "t_valid_waive_labels"
    id = x
    name = x
    retired = x
    update_at = x
    update_by = x
# * waive related end }


# * filter related begin {
class TFilters(Base):
    __tablename__ = "t_filters"
    id = x
    update_at = x
    update_by = x
    from_clk = x
    to_clk = x


class TFilterGroups(Base):
    __tablename__ = "t_filter_groups"
    id = x
    name = Column()
    wildcard = x
    update_at = x
    update_by = x
    update_repo = x
    update_branch = x
    update_revision = x


class TValidFilterLabels(Base):
    __tablename__ = "t_valid_filter_labels"
    id = x
    name = x
    retired = x
    update_at = x
    update_by = x
# * filter related end }